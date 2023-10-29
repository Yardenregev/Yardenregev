using System;
using System.Collections.Generic;
using Newtonsoft.Json;
using Udar.Web;
using UnityEngine;
using UnityEngine.UIElements;
using Zenject;

namespace Whisper.UI
{
    public class UIController : MonoBehaviour
    {
        [SerializeField] private UIDocument _uiDocument;
        [SerializeField] private VisualTreeAsset _bookmarkButtonTemplate;

        [Inject] private readonly IDialogUI _dialogUI;
        [Inject] private readonly ILoaderUI _loaderUI;
        [Inject] private readonly RecordRequestService _recordService;


        private ScrollView _bookmarksScrollView;
        private Button _startRecordingButton;
        private Button _stopRecordingButton;
        private void Awake()
        {
            _startRecordingButton = _uiDocument.rootVisualElement.Q<Button>("StartRecording_Button");
            _stopRecordingButton = _uiDocument.rootVisualElement.Q<Button>("StopRecording_Button");
            _bookmarksScrollView = _uiDocument.rootVisualElement.Q<ScrollView>("Bookmarks_ScrollView");
        }
        private void OnEnable()
        {
            _startRecordingButton.clicked += OnStartRecordingClicked;
            _stopRecordingButton.clicked += OnStopRecordingClicked;
        }
        private void OnDisable()
        {
            _startRecordingButton.clicked -= OnStartRecordingClicked;
            _stopRecordingButton.clicked -= OnStopRecordingClicked;
        }

        private async void OnStartRecordingClicked()
        {
            try
            {
                _loaderUI.Show("Start recording...");

                await _recordService.StartAsync();

                _startRecordingButton.style.display = DisplayStyle.None;
                _stopRecordingButton.style.display = DisplayStyle.Flex;
            }
            catch (WebException exe)
            {
                _dialogUI.Show("Something went wrong", exe.ErrorMessage + "\n" + "error code: " + exe.ErrorCode, null);
                Debug.LogErrorFormat(exe.ErrorMessage + ", error code= " + exe.ErrorCode);
                Debug.LogException(exe);
            }
            finally
            {
                _loaderUI.Hide();
            }

        }

        private async void OnStopRecordingClicked()
        {
            var request = new WebRequestData().SetURL(WebURL.URL, WeAPIMethods.GetStopRecording);

            try
            {
                _loaderUI.Show("Stop recording...");

                var dic = await _recordService.StopAsync();

                _startRecordingButton.style.display = DisplayStyle.Flex;
                _stopRecordingButton.style.display = DisplayStyle.None;

                _bookmarksScrollView.Clear();
                
                foreach (var item in dic)
                {
                    var elementInstance = _bookmarkButtonTemplate.Instantiate();
                    var timestampLabel = elementInstance.Q<Label>("Timestamp_Label");
                    var transcriptLabel = elementInstance.Q<Label>("Transcript_Label");

                    timestampLabel.text = item.Key;
                    transcriptLabel.text = item.Value;

                    _bookmarksScrollView.Add(elementInstance);
                }

            }
            catch (WebException exe)
            {
                _dialogUI.Show("Something went wrong", exe.ErrorMessage + "\n" + "error code: " + exe.ErrorCode, null);
                Debug.LogErrorFormat(exe.ErrorMessage + ", error code= " + exe.ErrorCode);
                Debug.LogException(exe);
            }
            finally
            {
                _loaderUI.Hide();
            }

        }

    }

}

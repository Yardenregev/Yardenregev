using System;
using System.Collections.Generic;
using Udar.Web;
using UnityEngine;
using UnityEngine.UIElements;
using Zenject;

namespace Whisper.UI
{
    public class UIController : MonoBehaviour
    {
        [SerializeField] private UIDocument _uiDocument;

        [Inject] private readonly IDialogUI _dialogUI;
        [Inject] private readonly ILoaderUI _loaderUI;
        [Inject] private readonly IWebService _webService;

        private Button _startRecordingButton;
        private Button _stopRecordingButton;
        private void Awake()
        {
            _startRecordingButton = _uiDocument.rootVisualElement.Q<Button>("StartRecording_Button");
            _stopRecordingButton = _uiDocument.rootVisualElement.Q<Button>("StopRecording_Button");
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
            var request = new WebRequestData().SetURL(WebURL.URL, WeAPIMethods.PostStartRecording);

            try
            {
                _loaderUI.Show("Start recording...");

                var result = await _webService.PostAync(request);

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

                var result = await _webService.GetAync(request);

                _startRecordingButton.style.display = DisplayStyle.Flex;
                _stopRecordingButton.style.display = DisplayStyle.None;

                var dic = JsonUtility.FromJson<Dictionary<string, string>>(result);
                Debug.Log(dic.Count);
                Debug.Log(result);
            }
            catch (WebException exe)
            {
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

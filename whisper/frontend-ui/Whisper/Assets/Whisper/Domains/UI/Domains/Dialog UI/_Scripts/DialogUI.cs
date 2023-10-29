using System;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UIElements;

namespace Whisper.UI
{
    public class DialogUI : MonoBehaviour, IDialogUI
    {
        [SerializeField] private UIDocument _uiDocument;

        private Button _okButton;
        private Label _titleLabel;
        private Label _bodyLabel;

        private Action _okCallback;

        private void Awake()
        {
            _okButton = _uiDocument.rootVisualElement.Q<Button>("Ok_Button");
            _titleLabel = _uiDocument.rootVisualElement.Q<Label>("Title_Label");
            _bodyLabel = _uiDocument.rootVisualElement.Q<Label>("Body_Label");

            Hide();
        }
        private void OnEnable()
        {
            _okButton.clicked += OnOkClicked;

        }

        private void OnDisable()
        {
            _okButton.clicked -= OnOkClicked;
        }


        private void OnOkClicked()
        {
            Hide();
            _okCallback?.Invoke();
        }

        public void Hide()
        {
            _uiDocument.rootVisualElement.style.display = DisplayStyle.None;

        }

        public void Show(string title, string body, Action okCallback)
        {
            _titleLabel.text = title;
            _bodyLabel.text = body;
            _okCallback = okCallback;

            _uiDocument.rootVisualElement.style.display = DisplayStyle.Flex;
        }
    }

}

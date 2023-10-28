using UnityEngine;
using UnityEngine.UIElements;

namespace Whisper.UI
{
    public class LoaderUI : MonoBehaviour, ILoaderUI
    {
        [SerializeField] private UIDocument _uiDocument;

        private Label _label;
        private void Awake()
        {
            _label = _uiDocument.rootVisualElement.Q<Label>("Label");
            Hide();
        }
        public void Hide()
        {
            _uiDocument.rootVisualElement.style.display = DisplayStyle.None;
        }

        public void Show(string text = "")
        {
            _uiDocument.rootVisualElement.style.display = DisplayStyle.Flex;

            _label.text = text;

        }
    }
}

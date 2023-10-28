using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UIElements;
using Zenject;

namespace Whisper.UI
{
    public class UIController : MonoBehaviour
    {
        [SerializeField] private UIDocument _uiDocument;

        [Inject] private IWebService _webService;

        private void OnEnable()
        {
            
        }
        private void OnDisable()
        {

        }

        private async void OnButtonClicked()
        {
            var request = new WebRequestData()
            {
                Url = "",
                Headers = new Dictionary<string, string>()
                {

                },

            };

            var result = await _webService.PostAync(request);
        }

    }
}

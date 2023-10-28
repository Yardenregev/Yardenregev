using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UIElements;

namespace Whisper.UI
{
    public class LoaderRotator : MonoBehaviour
    {
        [SerializeField] private UIDocument _uiDocument;
        [SerializeField] private string _elementName;
        [SerializeField] private float _speed;

        private VisualElement _element;
        private float _rotationAngle;

        private void Awake()
        {
            _element = _uiDocument.rootVisualElement.Q<VisualElement>(_elementName);
        }

        private void Update()
        {
            _rotationAngle += _speed * Time.deltaTime;
            _element.transform.rotation = Quaternion.Euler(0f, 0f, _rotationAngle);
            
            // Reset the rotation angle if it exceeds 360 degrees.
            if (_rotationAngle > 360f)
            {
                _rotationAngle = 0f;
            }
        }
    }

}

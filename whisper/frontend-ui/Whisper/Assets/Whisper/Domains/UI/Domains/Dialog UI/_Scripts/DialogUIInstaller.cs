using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using Zenject;

namespace Whisper.UI
{
    public class DialogUIInstaller : MonoInstaller
    {
        [SerializeField] private DialogUI _dialogUI;
        
        public override void InstallBindings()
        {
            Container.Bind<IDialogUI>().FromInstance(_dialogUI).AsSingle();
        }
    }

}

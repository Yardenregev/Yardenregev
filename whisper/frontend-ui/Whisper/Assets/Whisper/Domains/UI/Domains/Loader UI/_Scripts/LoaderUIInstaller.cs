using UnityEngine;
using Zenject;

namespace Whisper.UI
{
    public class LoaderUIInstaller : MonoInstaller
    {
        [SerializeField] private LoaderUI _loaderUI;

        public override void InstallBindings()
        {
            Container.Bind<ILoaderUI>().FromInstance(_loaderUI).AsSingle();
        }
    }
}

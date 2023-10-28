using Zenject;

namespace Whisper.Web
{
    public class WebSerivceInstaller:MonoInstaller
    {
        public override void InstallBindings()
        {
            Container.Bind<IWebService>().To<WebService>().AsSingle();
        }
    }
}

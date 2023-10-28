using Udar.Web;
using Zenject;

namespace Whisper
{
    public class WebSerivceInstaller : MonoInstaller
    {
        public override void InstallBindings()
        {
            Container.Bind<IWebService>().To<WebService>().AsSingle();
            Container.Bind<RecordRequestService>().ToSelf().AsSingle();
        }
    }
}

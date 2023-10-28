using System.Collections.Generic;
using System.Threading.Tasks;
using Newtonsoft.Json;
using Udar.Web;

namespace Whisper
{
    public class RecordRequestService
    {
        private readonly IWebService _webService;

        public RecordRequestService(IWebService webService)
        {
            _webService = webService;
        }
        public async Task StartAsync()
        {
            var request = new WebRequestData().SetURL(WebURL.URL, WeAPIMethods.PostStartRecording);

            var result = await _webService.PostAync(request);

        }
        public async Task<Dictionary<string, string>> StopAsync()
        {
            var request = new WebRequestData().SetURL(WebURL.URL, WeAPIMethods.GetStopRecording);

            var result = await _webService.GetAync(request);

            var dic = JsonConvert.DeserializeObject<Dictionary<string, string>>(result);

            return dic;
        }

    }
}

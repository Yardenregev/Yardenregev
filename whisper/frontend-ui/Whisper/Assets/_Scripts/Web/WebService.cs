using System.Net;
using System.Threading.Tasks;
using UnityEngine.Networking;

namespace Whisper
{
    public class WebService : IWebService
    {
        private void SetHeadersValues(UnityWebRequest request, WebRequestData requestData)
        {
            foreach (var header in requestData.Headers)
            {
                request.SetRequestHeader(header.Key, header.Value);
            }

        }

        public async Task<string> GetAync(WebRequestData requestData)
        {
            var webRequest = UnityWebRequest.Get(requestData.Url);
            SetHeadersValues(webRequest, requestData);

            webRequest.SendWebRequest();

            while (!webRequest.isDone)
                await Task.Yield();

            if (webRequest.result == UnityWebRequest.Result.ConnectionError || webRequest.result == UnityWebRequest.Result.ProtocolError)
            {
                throw new WebException(webRequest);
            }

            return webRequest.downloadHandler.text;
        }
        public async Task<string> PostAync(WebRequestData requestData)
        {
            var webRequest = UnityWebRequest.Post(requestData.Url, requestData.ObjectJSON);
            SetHeadersValues(webRequest, requestData);

            webRequest.SendWebRequest();

            while (!webRequest.isDone)
                await Task.Yield();

            if (webRequest.result == UnityWebRequest.Result.ConnectionError || webRequest.result == UnityWebRequest.Result.ProtocolError)
            {
                throw new WebException(webRequest);
            }

            return webRequest.downloadHandler.text;
        }
        public async Task<string> PutAync(WebRequestData requestData)
        {
            var webRequest = UnityWebRequest.Put(requestData.Url, requestData.ObjectJSON);
            SetHeadersValues(webRequest, requestData);

            webRequest.SendWebRequest();

            while (!webRequest.isDone)
                await Task.Yield();

            if (webRequest.result == UnityWebRequest.Result.ConnectionError || webRequest.result == UnityWebRequest.Result.ProtocolError)
            {
                throw new WebException(webRequest);
            }

            return webRequest.downloadHandler.text;
        }
        public async Task<string> DeleteAync(WebRequestData requestData)
        {
            var webRequest = UnityWebRequest.Delete(requestData.Url);
            SetHeadersValues(webRequest, requestData);

            webRequest.SendWebRequest();

            while (!webRequest.isDone)
                await Task.Yield();

            if (webRequest.result == UnityWebRequest.Result.ConnectionError || webRequest.result == UnityWebRequest.Result.ProtocolError)
            {
                throw new WebException(webRequest);
            }

            return webRequest.downloadHandler.text;
        }


    }


}

using System;
using UnityEngine.Networking;

namespace Udar.Web
{
    public class WebException : Exception
    {
        public UnityWebRequest Request;
        public long ErrorCode => Request.responseCode;
        public string ErrorMessage => Request.downloadHandler.text;
        public WebException(UnityWebRequest request)
        {
            Request = request;
        }
    }
    

}

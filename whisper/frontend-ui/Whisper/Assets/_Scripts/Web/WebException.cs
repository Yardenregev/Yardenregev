using System;
using UnityEngine.Networking;

namespace Whisper
{
    public class WebException : Exception
    {
        public UnityWebRequest Request;
        public long ErrorCode => Request.responseCode;
        public string ErrorMessage => Request.error;
        public WebException(UnityWebRequest request)
        {
            Request = request;
        }
    }
    

}

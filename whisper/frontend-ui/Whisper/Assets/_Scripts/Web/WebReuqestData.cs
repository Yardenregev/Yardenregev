using System.Collections.Generic;

namespace Whisper
{
    public struct WebRequestData
    {
        public string Url;
        public Dictionary<string,string> Headers;//Key=header,value=value
        public string ObjectJSON;
    }

}

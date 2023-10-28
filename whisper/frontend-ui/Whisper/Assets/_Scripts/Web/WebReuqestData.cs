using System.Collections.Generic;

namespace Udar.Web
{
    public class WebRequestData
    {
        public string Url;
        public Dictionary<string, string> Headers = new Dictionary<string, string>();//Key=header,value=value
        public string ObjectJSON;

        public WebRequestData SetURL(string url, string method)
        {
            Url = url + method;

            return this;
        }
        public WebRequestData AddHeader(string header,string value)
        {
            Headers.Add(header,value);
            
            return this;
        }
    }

}

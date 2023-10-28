using System.Collections;
using System.Threading.Tasks;
using UnityEngine;

namespace Whisper
{
    public interface IWebService
    {
        public Task<string> PostAync(WebRequestData requestData);
        public Task<string> GetAync(WebRequestData requestData); 
        public Task<string> DeleteAync(WebRequestData requestData);
        public Task<string> PutAync(WebRequestData requestData);


    }

}

using System.Collections;
using System.Collections.Generic;

namespace Whisper.UI
{
    public interface ILoaderUI
    {
        public void Show(string text = "");
        public void Hide();
    }
}

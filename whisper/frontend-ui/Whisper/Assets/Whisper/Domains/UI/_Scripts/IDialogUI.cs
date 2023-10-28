using System;

namespace Whisper.UI
{
    public interface IDialogUI
    {
        public void Show(string header, string body, Action okCallback);
        public void Hide();
    }
  
}

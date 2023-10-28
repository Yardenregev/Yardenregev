using System;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

namespace Whisper.UI
{
    public interface IDialogUI 
    {
       public void Show(string header,string body,Action okCallback);
       public void Hide();
    }
}

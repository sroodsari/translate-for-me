import { useState } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [text, setText] = useState('');
  const [language, setLanguage] = useState('zh-CN'); // 'zh-cn' or 'fa'
  const [translatedLines, setTranslatedLines] = useState([]);
  const [transliteratedLines, setTransliteratedLines] = useState([]);

  const translateText = async () => {
    try {
      const lines = text.split('\n');

      const response = await axios.post(`${process.env.REACT_APP_BACKEND_URL}/translate`, {
        lines,
        from_lang: language,
        to_lang: 'en',
      }, {
        headers: {
          "Content-Type": "application/json"
        }
      });

      setTranslatedLines(response.data.translated);
      setTransliteratedLines(response.data.transliterated);
    } catch (error) {
      console.error('Error translating text:', error.response ? error.response.data : error.message);
      setTranslatedLines(['Translation failed. Please try again.']);
      setTransliteratedLines(['Transliteration failed. Please try again.']);
    }
  };

  return (
    <div className="App">
      <header className="App-header">
        <h2>translate for me</h2>
      </header>
      <hr className="hr" />
      <div className="App-container">
        <div className="container-header">
          <h1>{language === 'zh-CN' ? 'Chinese to English' : 'Farsi to English'} Translator</h1>
          <label>
            Language:
            <select value={language} onChange={(e) => setLanguage(e.target.value)}>
              <option value="zh-CN">Chinese</option>
              <option value="fa-IR">Farsi</option>
            </select>
          </label>
        </div>

        <div className="column-container">
          <div className="column-left">
            <textarea
              rows="10"
              cols="100"
              placeholder={language === 'zh-CN' ? "Enter Chinese text" : "Enter Farsi text"}
              value={text}
              onChange={(e) => setText(e.target.value)}
            />
            <div className='userSelection'>


              <button onClick={translateText}>Translate</button>
            </div>

          </div>
          <br />
          <div className="column-right">
            <div className="translation-container">
              {text.split('\n').map((line, index) => (
                <div key={index} className="translation-item">
                  <p className="original-text">{line}</p>
                  <p className="transliterated-text">{transliteratedLines[index]}</p>
                  <p className="translated-text">{translatedLines[index]}</p>
                </div>
              ))}
            </div>
          </div>
        </div>
      </div>

    </div >
  );
}

export default App;

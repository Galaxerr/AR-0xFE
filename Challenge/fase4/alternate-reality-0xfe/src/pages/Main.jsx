import React, { useState } from 'react';
import '../css/Main.css';

const flag = "Y0u_4c7u4lly_D1d_I7_Y0u_M4d7l4d";

function Main() {
  const [inputFlag, setInputFlag] = useState('');
  const finalFlag = "UNIFE{C0n6r47z_On_834t1ng_7h3_ARG}";
  const [error, setError] = useState('');
  
  const [showPopup, setShowPopup] = useState(false);
  const [animateExit, setAnimateExit] = useState(false);

  const handleClose = () => {
    setAnimateExit(true);
  };

  const handleAnimationEnd = () => {
    if (animateExit) {
      setShowPopup(false);
      setAnimateExit(false);
    }
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    if (inputFlag === flag) {
      setShowPopup(true);
    } else {
      setError('Incorrect flag.');
    }
  };


  return (
    <div className="main-container">
      <h1>Alternate Reality 0xFE</h1>
      <h2>Welcome, player</h2>
      <p>
        This is the final step to get you to the flag. Fear not, for it is almost over
      </p>
      <p>
        The flag for this final phase is stored somewhere you have already seen, you just have to find <br />
        all the pieces. You were brought here by the last piece, so you already know what to do.
      </p>
      <p> May luck be on your side. (<strong>Remember, the flag is non-standard</strong>)</p>
      <div class="flag-submit">
        <form onSubmit={handleSubmit}>
          <input
            type="text"
            value={inputFlag}
            onChange={(e) => setInputFlag(e.target.value)}
            placeholder=". . ."
          />
          <button type="submit">Submit</button>
        </form>
      </div>

      {showPopup && (
        <div 
          className={`popup ${animateExit ? "popup-exit" : "popup-enter"}`} 
          onAnimationEnd={handleAnimationEnd}
        >
          <div className="popup-content">
            <h2>Congratulations!</h2>
            <p>You have completed all the phases!</p>
            <p>here is you hard-earned reward: <strong>{finalFlag}</strong></p>
            <button onClick={handleClose}>Close</button>
          </div>
        </div>
      )}
      {error && <p className="error">{error}</p>}
    </div>
  );
}

export default Main;

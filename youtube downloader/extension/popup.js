document.getElementById('get-video').addEventListener('click', () => {
    browser.tabs.query({ active: true, currentWindow: true }, (tabs) => {
      const url = tabs[0].url;
  
      fetch('http://localhost:7868/get_video', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ url: url })
      }).then(response => {
        if (response.ok) {
          console.log('URL sent to Python server successfully.');
        } else {
          console.error('Failed to send URL to Python server.');
        }
      }).catch(error => {
        console.error('Error:', error);
      });
    });
  });

  document.getElementById('get-audio').addEventListener('click', () => {
    browser.tabs.query({ active: true, currentWindow: true }, (tabs) => {
      const url = tabs[0].url;
  
      fetch('http://localhost:7868/get_audio', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ url: url })
      }).then(response => {
        if (response.ok) {
          console.log('URL sent to Python server successfully.');
        } else {
          console.error('Failed to send URL to Python server.');
        }
      }).catch(error => {
        console.error('Error:', error);
      });
    });
  });
  
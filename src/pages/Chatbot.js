import React, { useState } from 'react';
import axios from 'axios';

const Chatbot = () => {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState('');
  const [loading, setLoading] = useState(false);

  const sendMessage = async () => {
    if (!input.trim()) return;

    const userMessage = { text: input, sender: 'user' };
    setMessages([...messages, userMessage]);
    setInput('');
    setLoading(true);

    try {
      const response = await axios.post('http://localhost:5000/api/chatbot/chat', { message: input });
      const botMessage = { text: response.data.response, sender: 'bot' };
      setMessages(prevMessages => [...prevMessages, botMessage]);
    } catch (error) {
      console.error('Error sending message:', error);
      const errorMessage = { text: 'Sorry, I encountered an error. Please try again.', sender: 'bot' };
      setMessages(prevMessages => [...prevMessages, errorMessage]);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="container mx-auto p-4">
      <h2 className="text-2xl font-bold mb-4">Chat with SafeHer</h2>
      <div className="bg-gray-100 p-4 h-96 overflow-y-auto mb-4 rounded">
        {messages.map((message, index) => (
          <div key={index} className={`mb-2 ${message.sender === 'user' ? 'text-right' : 'text-left'}`}>
            <span className={`inline-block p-2 rounded ${message.sender === 'user' ? 'bg-blue-500 text-white' : 'bg-white'}`}>
              {message.text}
            </span>
          </div>
        ))}
        {loading && <div className="text-center">SafeHer is typing...</div>}
      </div>
      <div className="flex">
        <input
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          className="flex-grow p-2 border rounded-l"
          placeholder="Type your message..."
        />
        <button
          onClick={sendMessage}
          disabled={loading}
          className={`bg-blue-500 text-white p-2 rounded-r ${loading ? 'opacity-50 cursor-not-allowed' : ''}`}
        >
          Send
        </button>
      </div>
    </div>
  );
};

export default Chatbot;
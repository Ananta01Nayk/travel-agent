import { useState } from "react";
import api from "../services/api";

export default function useChat() {

  const [messages, setMessages] = useState([
    {
      role: "assistant",
      content:
        "Hello 👋 I'm Bharti, your AI travel assistant. Where would you like to travel today?",
    },
  ]);

  const [sources, setSources] = useState([]);

  const [loading, setLoading] = useState(false);

  const sendMessage = async (question) => {

    if (!question.trim()) return;

    const userMessage = {
      role: "user",
      content: question,
    };

    setMessages((prev) => [...prev, userMessage]);

    setLoading(true);

    try {

      const response = await api.post("/chat", {
        question: question,
      });

      setMessages((prev) => [
        ...prev,
        {
          role: "assistant",
          content: response.data.answer,
        },
      ]);

      setSources(response.data.sources);

    } catch (err) {

      setMessages((prev) => [
        ...prev,
        {
          role: "assistant",
          content: "Something went wrong.",
        },
      ]);

      console.log(err);

    } finally {

      setLoading(false);

    }
  };

  return {
    messages,
    sources,
    loading,
    sendMessage,
  };
}
import { useState } from "react";
import { SendHorizonal } from "lucide-react";

export default function ChatInput({ sendMessage, loading }) {
  const [question, setQuestion] = useState("");

  const handleSubmit = () => {
    console.log("===== ChatInput =====");
    console.log("Button clicked");
    console.log("Question:", question);
    console.log("sendMessage:", sendMessage);

    if (!question.trim()) {
      console.log("Question is empty");
      return;
    }

    if (typeof sendMessage !== "function") {
      console.error("sendMessage is NOT a function");
      return;
    }

    sendMessage(question);

    setQuestion("");
  };

  return (
    <div className="border-t p-5">
      <div className="flex gap-3">
        <input
          value={question}
          onChange={(e) => setQuestion(e.target.value)}
          onKeyDown={(e) => {
            if (e.key === "Enter") {
              handleSubmit();
            }
          }}
          className="flex-1 border rounded-full px-6 py-4 outline-none"
          placeholder="Ask about your next trip..."
        />

        <button
          type="button"
          onClick={handleSubmit}
          disabled={loading}
          className="w-14 h-14 rounded-full bg-blue-600 text-white flex items-center justify-center"
        >
          <SendHorizonal size={22} />
        </button>
      </div>
    </div>
  );
}
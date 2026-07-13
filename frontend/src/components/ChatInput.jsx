import { useState } from "react";
import { SendHorizonal, Paperclip, Mic } from "lucide-react";

export default function ChatInput({
  sendMessage,
  loading,
}) {
  const [question, setQuestion] = useState("");

  const handleSubmit = () => {
    if (!question.trim()) return;

    sendMessage(question);
    setQuestion("");
  };

  return (
    <div
      className="
        rounded-[26px]
        bg-white/95
        backdrop-blur-xl
        shadow-[0_15px_40px_rgba(0,0,0,.15)]
        border
        border-white/40
        px-5
        py-2
      "
    >
      <div className="flex items-center gap-2">

        {/* Attachment */}

        <button
          className="
            w-11
            h-11
            rounded-xl
            hover:bg-slate-100
            transition
            flex
            items-center
            justify-center
          "
        >
          <Paperclip
            size={18}
            className="text-slate-500"
          />
        </button>

        {/* Input */}

        <input
          value={question}
          onChange={(e) => setQuestion(e.target.value)}
          onKeyDown={(e) => {
            if (e.key === "Enter" && !loading) {
              e.preventDefault();
              handleSubmit();
            }
          }}
          placeholder="Where would you like to travel?"
         className="
          flex-1
          bg-transparent
          outline-none
          text-[15px]
          text-slate-700
          placeholder:text-slate-400
          px-2
        "
        />

        {/* Voice (future feature) */}

        <button
          className="
            w-11
            h-11
            rounded-xl
            hover:bg-slate-100
            transition
            flex
            items-center
            justify-center
          "
        >
          <Mic
            size={18}
            className="text-slate-500"
          />
        </button>

        {/* Send */}

        <button
          onClick={handleSubmit}
          disabled={loading}
          className="
          w-10
          h-10
          rounded-lg
          bg-blue-600
          hover:bg-blue-700
          text-white
          flex
          items-center
          justify-center
          transition-all
          duration-200
          disabled:opacity-50
          disabled:cursor-not-allowed
        "
        >
          {loading ? (
            <div className="w-5 h-5 rounded-full border-2 border-white border-t-transparent animate-spin" />
          ) : (
            <SendHorizonal size={18} strokeWidth={2.2} />
          )}
        </button>

      </div>
    </div>
  );
}
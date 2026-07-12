import { Bot, User } from "lucide-react";
import ReactMarkdown from "react-markdown";
import remarkGfm from "remark-gfm";

export default function ChatMessage({ role, content }) {
  const isUser = role === "user";

  return (
    <div
      className={`flex mb-6 ${
        isUser ? "justify-end" : "justify-start"
      }`}
    >
      <div
        className={`flex gap-3 max-w-[75%] ${
          isUser ? "flex-row-reverse" : ""
        }`}
      >
        {/* Avatar */}

        <div
          className={`w-11 h-11 rounded-full flex items-center justify-center shadow-md
          ${
            isUser
              ? "bg-blue-600 text-white"
              : "bg-white border"
          }`}
        >
          {isUser ? <User size={20} /> : <Bot size={20} />}
        </div>

        {/* Bubble */}

        <div
          className={`rounded-3xl px-5 py-4 shadow-md
          ${
            isUser
              ? "bg-blue-600 text-white"
              : "bg-white text-gray-800"
          }`}
        >
          <p className="leading-7 whitespace-pre-wrap">
            <ReactMarkdown remarkPlugins={[remarkGfm]}>
                {content}
            </ReactMarkdown>
          </p>
        </div>
      </div>
    </div>
  );
}
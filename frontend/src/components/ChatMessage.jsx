import robot from "../assets/robot.png";

export default function ChatMessage({ message }) {
  const isUser = message.role === "user";

  return (
    <div
      className={`flex ${
        isUser ? "justify-end" : "justify-start"
      }`}
    >
      {!isUser && (
        <img
          src={robot}
          alt=""
          className="
            w-10
            h-10
            rounded-full
            bg-white
            p-1
            mr-3
            mt-1
            shadow-md
            flex-shrink-0
          "
        />
      )}

      <div
        className={`
          max-w-[580px]
          rounded-3xl
          px-6
          py-4
          shadow-lg
          ${
            isUser
              ? "bg-blue-600"
              : "bg-white text-gray-800"
          }
        `}
      >
        {!isUser && (
          <p className="text-slate-500 text-[11px] font-medium mb-2">
            Bharti
          </p>
        )}

        <p className="text-[16px] leading-7 whitespace-pre-wrap">
          {message.content}
        </p>

        <div
          className={`mt-3 text-[11px] ${
            isUser
              ? "text-blue-100"
              : "text-gray-400"
          } text-right`}
        >
          {new Date().toLocaleTimeString([], {
            hour: "2-digit",
            minute: "2-digit",
          })}
        </div>
      </div>
    </div>
  );
}
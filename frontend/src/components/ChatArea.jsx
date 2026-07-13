import ChatMessage from "./ChatMessage";
import TypingIndicator from "./TypingIndicator";

export default function ChatArea({
  messages,
  loading,
}) {
  return (
    <div
      className="
        h-full
        overflow-y-auto
        pr-4
        pt-2
        pb-2
      "
    >
      <div
        className="
          max-w-[760px]
          space-y-8
        "
      >
        {messages.map((message, index) => (
          <ChatMessage
            key={index}
            message={message}
          />
        ))}

        {loading && <TypingIndicator />}
      </div>
    </div>
  );
}
export default function TypingIndicator() {
  return (
    <div className="flex justify-start mt-6">
      <div className="bg-white rounded-3xl shadow-lg px-6 py-4 flex items-center gap-2">
        <span
          className="w-3 h-3 rounded-full bg-blue-500 animate-bounce"
          style={{ animationDelay: "0s" }}
        ></span>

        <span
          className="w-3 h-3 rounded-full bg-blue-500 animate-bounce"
          style={{ animationDelay: "0.15s" }}
        ></span>

        <span
          className="w-3 h-3 rounded-full bg-blue-500 animate-bounce"
          style={{ animationDelay: "0.3s" }}
        ></span>

        <span className="ml-3 text-gray-500 text-sm">
          Bharti is typing...
        </span>
      </div>
    </div>
  );
}
import AgentWindow from "./components/AgentWindow";
import RetrievalSidebar from "./components/RetrievalSidebar";
import useChat from "./hooks/useChat";

import heroBg from "./assets/hero-bg.png";

export default function App() {
  const {
    messages,
    loading,
    sendMessage,
    sources,
  } = useChat();

  return (
    <div className="relative w-screen h-screen overflow-hidden">

      {/* Background */}
      <img
        src={heroBg}
        alt="Background"
        className="absolute inset-0 w-full h-full object-cover"
      />

      {/* Overlay */}
      <div className="absolute inset-0 bg-black/20 backdrop-blur-[1px]" />

      {/* Main Content */}
      <div className="relative z-10 h-full px-8 py-8">

        <div
         className={`
          h-full
          max-w-[1650px]
          mx-auto
          grid
          ${sources && sources.length > 0
              ? "grid-cols-[1fr_390px]"
              : "grid-cols-1"}
          gap-8
          transition-all
          duration-300
        `}
        >
          {/* Chat */}
          <AgentWindow
            messages={messages}
            loading={loading}
            sendMessage={sendMessage}
          />

          {/* AI Recommendations */}
          {sources && sources.length > 0 && (
          <RetrievalSidebar
            sources={sources}
          />
            )}

        </div>

      </div>

    </div>
  );
}
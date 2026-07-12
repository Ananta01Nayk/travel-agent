import Header from "./components/Header";
import AgentWindow from "./components/AgentWindow";
import RetrievalSidebar from "./components/RetrievalSidebar";
import useChat from "./hooks/useChat";

export default function App() {

  const {
    messages,
    loading,
    sendMessage,
    sources
  } = useChat();

  return (

    <div className="bg-slate-100 h-screen overflow-hidden">

      <Header />

      <div className="flex h-[calc(100vh-90px)] overflow-hidden p-6 gap-6">

        <div className="flex-1 h-full overflow-hidden">

          <AgentWindow
            messages={messages}
            loading={loading}
            sendMessage={sendMessage}
          />

        </div>

        <div className="w-[360px] h-full flex-shrink-0">

          <RetrievalSidebar
            sources={sources}
          />

        </div>

      </div>

    </div>

  );

}
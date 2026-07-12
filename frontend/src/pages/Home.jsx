import Header from "../components/Header";
import AgentWindow from "../components/AgentWindow";
import RetrievalSidebar from "../components/RetrievalSidebar";
import useChat from "../hooks/useChat";

export default function Home() {

  const {
    messages,
    sources,
    loading,
    sendMessage,
  } = useChat();

  return (

    <div className="min-h-screen bg-[#F3F7FC]">

      <Header />

      <main className="max-w-[1500px] mx-auto px-8 py-10">

        <div className="grid grid-cols-12 gap-8 h-[82vh]">

          <div className="col-span-9">

            <AgentWindow
              messages={messages}
              loading={loading}
              sendMessage={sendMessage}
            />

          </div>

          <div className="col-span-3">

            <RetrievalSidebar
              sources={sources}
            />

          </div>

        </div>

      </main>

    </div>

  );

}
import ChatArea from "./ChatArea";
import ChatInput from "./ChatInput";

export default function AgentWindow({

  messages,
  loading,
  sendMessage

}) {

  return (

    <div className="bg-white rounded-[30px] shadow-xl h-full flex flex-col overflow-hidden">

      <div className="border-b px-8 py-5">

        <h2 className="font-bold text-xl">
          Namaste India Trip Agent
        </h2>

        <p className="text-gray-500">
          Ask anything about tours.
        </p>

      </div>

      <div className="flex-1 overflow-hidden">

        <ChatArea
          messages={messages}
        />

      </div>

      <ChatInput

        sendMessage={sendMessage}
        loading={loading}

      />

    </div>

  );

}
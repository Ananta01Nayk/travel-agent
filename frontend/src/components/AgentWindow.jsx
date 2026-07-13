import robot from "../assets/robot.png";

import ChatArea from "./ChatArea";
import ChatInput from "./ChatInput";

export default function AgentWindow({
  messages,
  loading,
  sendMessage,
}) {
  return (
    <div
      className="
        relative
        h-full
        rounded-[32px]
        bg-white/10
        backdrop-blur-xl
        border border-white/20
        shadow-[0_25px_70px_rgba(0,0,0,.35)]
        overflow-hidden
        flex
        flex-col
      "
    >
      {/* Header */}

      <div
        className="
          h-[70px]
          px-7
          flex
          items-center
          justify-between
          border-b
          border-white/10
          bg-white/5
        "
      >
        <div className="flex items-center gap-4">

          <div className="w-12 h-12 rounded-full bg-white flex items-center justify-center shadow-md">
            <img
              src={robot}
              alt="Bharti"
              className="w-9 h-9 object-contain"
            />
          </div>

          <div>

            <h2 className="text-white text-[24px] font-semibold leading-none">
              Namaste India Trip Agent
            </h2>

            <div className="flex items-center gap-2 mt-2">

              <span className="w-2.5 h-2.5 rounded-full bg-green-400 animate-pulse"></span>

              <span className="text-white/80 text-sm">
                Online · AI Agent
              </span>

            </div>

          </div>

        </div>

        <button
          className="
            w-10
            h-10
            rounded-xl
            bg-white/10
            hover:bg-white/20
            text-white
            text-2xl
            transition
          "
        >
          ×
        </button>

      </div>

      {/* Chat Body */}

      <div className="relative flex-1 overflow-hidden">

        {/* Chat */}

        <div
          className="
            absolute
            inset-0
            px-8
            pt-8
            pb-[100px]
          "
        >
          <ChatArea
            messages={messages}
            loading={loading}
          />
        </div>

        {/* Input */}

        <div
          className="
            absolute
            left-8
            right-8
            bottom-6
            z-30
          "
        >
          <ChatInput
            sendMessage={sendMessage}
            loading={loading}
          />
        </div>

      </div>

    </div>
  );
}
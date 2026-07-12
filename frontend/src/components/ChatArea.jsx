import { useEffect, useRef } from "react";
import ChatMessage from "./ChatMessage";

export default function ChatArea({ messages }) {

  const bottomRef = useRef(null);

  useEffect(() => {

    bottomRef.current?.scrollIntoView({
      behavior: "smooth"
    });

  }, [messages]);

  return (

    <div className="h-full overflow-y-auto px-8 py-8">

      {messages.map((msg, index) => (

        <ChatMessage

          key={index}
          role={msg.role}
          content={msg.content}

        />

      ))}

      <div ref={bottomRef}></div>

    </div>

  );

}
import * as React from "react";
export default function TomatoLogo() {
    return (
        <svg
            xmlns="http://www.w3.org/2000/svg"
            width={80}
            height={80}
            viewBox="0 0 256 256"
        >
            <circle cx={128} cy={128} r={80} fill="#b61500" strokeWidth={8} />
            <line x1={131} y1={133} x2={88} y2={108} stroke="white" strokeWidth={6} />
            <line x1={129} y1={132} x2={163} y2={138} stroke="white" strokeWidth={6} />
            <path
                d="m300,-90 q-20,20 0,60 q20,-20 0,-60"
                fill="green"
                transform="rotate(56, 147, -91)"
            />
            <path
                d="m300,-90 q-20,20 0,60 q20,-20 0,-60"
                fill="green"
                transform="rotate(150, 220, -26)"
            />
        </svg>
    );
}
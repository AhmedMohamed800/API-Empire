import React from "react";
import { useEffect, useState } from "react";
import axios from "axios";
import Cookies from "js-cookie";
import { useNavigate } from "react-router-dom";

interface Req {
  available_req: number;
  max_req: number;
  used_req: number;
}

const Billing = () => {
  const navigate = useNavigate();
  const [reqs, setReqs] = useState<Req>({
    available_req: 0,
    max_req: 0,
    used_req: 0,
  });
  const [noKey, Setkey] = useState<boolean>(false);

  useEffect(() => {
    const requestURL = `${process.env.REACT_APP_API_URL}/api/v1/reqs`;
    const session = Cookies.get("session");
    if (session) {
      axios
        .get(requestURL, { headers: { "session-id": JSON.parse(session) } })
        .then((res) => {
          console.log(res.data);
          if (res.data.available_req === 0) {
            navigate("/buyreqs");
          }
          setReqs(res.data.data);
        })
        .catch((err) => {
          Setkey(true);
        });
    }
  }, []);

  return (
    <div className="relative z-10">
      <section className={`${noKey && "hidden"}`}>
        <p>hello</p>
      </section>
      <h1
        className={`${noKey || "hidden"} absolute left-[50%] top-[50%] translate-x-[-50%] translate-y-[-50%] text-center text-5xl`}
      >
        Go to User and generate a key
      </h1>
    </div>
  );
};

export default Billing;

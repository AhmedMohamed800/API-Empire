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

  useEffect(() => {
    const requestURL = `${process.env.REACT_APP_API_URL}/api/v1/reqs`;
    const session = Cookies.get("session");
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
        console.log(err);
      });
  }, []);

  return <div>{/* <PayPalButtons /> */}</div>;
};

export default Billing;

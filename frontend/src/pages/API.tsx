import React from "react";
import { useParams } from "react-router-dom";
import { useEffect, useState } from "react";
import axios from "axios";

interface APIProps {
  api_id: number;
  category: string;
  description: string;
  id: number;
  method: string;
  response_ex: string;
  title: string;
  url: string;
}

const API = () => {
  const [endpoint, setEndpoint] = useState<APIProps[]>([]);
  const { id } = useParams();

  useEffect(() => {
    const URL = `${process.env.REACT_APP_API_URL}/api/v1/service/${id}`;
    axios.get(URL).then((response) => {
      setEndpoint(response.data);
    });
    document.title = "API";
  }, []);

  return (
    <section className="z-10 mx-20 flex  flex-col max-sm:mx-5">{id}</section>
  );
};

export default API;

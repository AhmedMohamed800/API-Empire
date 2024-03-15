import React from "react";
import { useNavigate } from "react-router-dom";

interface APICardProps {
  title: string;
  description: string;
  image_cover: string;
  url: string;
  category: string;
}

const APICard: React.FC<APICardProps> = ({
  title,
  description,
  image_cover,
  url,
  category,
}) => {
  const navigate = useNavigate();

  function handleConnect() {
    navigate(`/API/${url}`);
  }

  return (
    <div
      onClick={handleConnect}
      className="api-card relative flex cursor-pointer flex-col gap-2 overflow-hidden rounded-md border-2 border-neutral-400 p-3 "
    >
      <div
        style={{
          backgroundImage: `linear-gradient(180deg, rgba(99, 91, 255, 0) 0%, rgba(99, 91, 255, 0.5) 100%), url(${image_cover})`,
        }}
        className="h-40 w-full rounded-md border-2 border-neutral-400 bg-cover bg-center bg-no-repeat "
      ></div>
      <h4 className=" border-b-2 border-white pb-2 text-center  font-semibold">
        {title}
      </h4>
      <p className=" text-sm text-neutral-300">{description}</p>
      <div className="flex items-center justify-between gap-2">
        <button className="  rounded-md  bg-primary px-3 py-2 text-white">
          Connect
        </button>
        <p className="text-sm">Free 7-day trial</p>
      </div>
      <p className=" absolute -right-4 top-2 rotate-45 bg-neutral-400 px-3 text-[10px]">
        {category}
      </p>
    </div>
  );
};

export default APICard;

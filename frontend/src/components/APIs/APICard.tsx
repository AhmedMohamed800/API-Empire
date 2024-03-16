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
      className="api-card group relative flex h-[320px] cursor-pointer  flex-col gap-2 overflow-hidden rounded-md border-2 border-neutral-400 p-3 hover:border-primary "
    >
      <div
        style={{
          backgroundImage: `linear-gradient(180deg, rgba(136, 136, 136, 0.00) 0%, rgba(136, 136, 136, 0.50) 93.5%), url(${image_cover})`,
        }}
        className="h-40 w-full rounded-md border-2 border-neutral-400 bg-cover bg-center bg-no-repeat group-hover:border-primary "
        onMouseOver={(e) =>
          (e.currentTarget.style.backgroundImage = `"linear-gradient(180deg, rgba(99, 91, 255, 0.00) 0%, rgba(99, 91, 255, 0.50) 100%), url(${image_cover})`)
        }
        onMouseOut={(e) =>
          (e.currentTarget.style.backgroundImage = `linear-gradient(180deg, rgba(136, 136, 136, 0.00) 0%, rgba(136, 136, 136, 0.50) 93.5%), url(${image_cover})`)
        }
      ></div>
      <h4 className=" border-b-2 border-white pb-2 text-center  font-semibold capitalize">
        {title}
      </h4>
      <p
        className=" overflow-hidden  text-sm text-neutral-300"
        style={{
          display: "-webkit-box",
          WebkitLineClamp: 2,
          WebkitBoxOrient: "vertical",
          maxWidth: "200ch",
        }}
      >
        {description}
      </p>
      <div className="flex items-center justify-between gap-2">
        <button className="  rounded-md  bg-neutral-400 px-3 py-2 text-white group-hover:bg-primary">
          Connect
        </button>
        <p className="text-sm">Free 7-day trial</p>
      </div>
      <p className=" absolute -right-4 top-2 rotate-45 bg-neutral-400 px-3 text-[10px] group-hover:bg-primary">
        {category}
      </p>
    </div>
  );
};

export default APICard;

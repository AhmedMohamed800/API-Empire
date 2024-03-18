import React, { useState, useEffect } from "react";
const arrow = require("../../assets/apis/arrow.svg") as string;
import Skeleton from "react-loading-skeleton";

const Table = ({ header, content, generateUUID }) => {
  const [isLoading, setIsLoading] = useState(true);

  useEffect(() => {
    if (content.length > 0) {
      setIsLoading(false);
    }
  }, [content]);

  const noContent = (
    <tr key={generateUUID()} className="tr">
      {header.map((key) => (
        <td className="td" key={generateUUID()}>
          -
        </td>
      ))}
    </tr>
  );

  return (
    <div className=" overflow-x-auto">
      <table className="w-full bg-black">
        <thead>
          <tr className="tr">
            {header.map((head) => {
              return (
                <th
                  key={head}
                  className={`td  ${head.length <= 3 ? "uppercase" : "capitalize"}`}
                >
                  {head}
                </th>
              );
            })}
          </tr>
        </thead>
        <tbody>
          {isLoading ? (
            <tr className="tr">
              {header.map((key) => (
                <td className="td" key={generateUUID()}>
                  <Skeleton count={1} />
                </td>
              ))}
            </tr>
          ) : content.length > 0 ? (
            content.map((data) => {
              return (
                <tr key={generateUUID()} className="tr">
                  {header.map((key) => (
                    <td className="td" key={generateUUID()}>
                      {data[key]}
                    </td>
                  ))}
                </tr>
              );
            })
          ) : (
            noContent
          )}
        </tbody>
      </table>
    </div>
  );
};

export default Table;

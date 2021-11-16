import React, {
  useState,
  useEffect } from "react";
import { useLocation } from "react-router-dom";

import "../css/style.css";
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faFilePowerpoint } from '@fortawesome/free-solid-svg-icons'


export default function DownloadPptBtn({ to, ...props }) {
  let location = useLocation();
  let pathname = location.pathname.slice(1).split("/")
  const report = pathname[0]
  const reportId = pathname[1]

  const [file, setFile] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetch(`http://172.20.0.4:5000/file/${report}/pptx/${reportId}`)
    .then(res => {
      if (res.ok) {
        return new Blob([res], { type: 'application/octet-stream' })
      }
      throw res;
    })
    .then(blob => setFile(blob))
    .catch((error) => {
      console.error("Error downloading report: ", error);
      setError(error);
    })
    .finally(() => {
      setLoading(false);
    });
  }, [report, reportId]);

  if (loading) return "Loading...";
  if (error) return "Error!";

  return <button onClick={() => {
    const url = URL.createObjectURL(file)
    const link = document.createElement('a');
    link.href = url;
    link.innerText = 'Download file';
    link.setAttribute('download', `${report}.pptx`);
    link.click();
    }}
    className="download-btn ppt-btn"
  >
    <FontAwesomeIcon icon={faFilePowerpoint} size="2x" />
  </button>;
}
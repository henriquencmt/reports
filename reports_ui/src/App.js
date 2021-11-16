import { Outlet, Link } from "react-router-dom";

export default function App() {
  return (
    <div>
      <div className="header">
        <a href="/home" className="title-link">
          <div className="title-box">
            reports
          </div>
        </a>
      </div>

      <nav className="nav-bar">
        <Link to="daily" className="nav-bar-link">
          <div className="nav-bar-box">
            Daily
          </div>
        </Link>

        <Link to="monthly" className="nav-bar-link">
          <div className="nav-bar-box">
            Monthly
          </div>
        </Link>
      </nav>

      <Outlet />
    </div>
  );
}
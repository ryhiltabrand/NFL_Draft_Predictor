import axios from "axios"
import { useEffect, useState } from "react";
import "./TeamStats.css"

function TeamStats(props) {
    var team = props.team;
    const host = window.location.hostname;
    const port = 8000;

    const [stats, setStats] = useState([]);
    //const [roster, setRoster] = useState([]);
    const [loaded, setLoaded] = useState(false);

    useEffect(() => {
        axios.get(`http://${host}:${port}/data/${team.acryonm}/`).then((res) => {
            setStats(res.data)
            setLoaded(true);

        })
    }, []);

    return (
        <div>
            
            {
                loaded ? stats.map((stat) =>
                    <div class="flexbox-container">
                        Team stats:
                        <div>Team: {stat["Team"][0]['name']}</div>
                        <div> Wins: {stat["Team"][0]['wins']} </div>
                        <div>Losses: {stat["Team"][0]['losses']} </div>
                        <div>Points For: {stat["Team"][0]['pointsFor']} </div>
                        <div>Points Against: {stat["Team"][0]['pointsAgainst']} </div>
                        <div>Yards For: {stat["Team"][0]['yardsFor']}</div>
                        <div>Yards Against: {stat["Team"][0]['yardsAgainst']}</div>
                    </div>
                ) : ""
            }

        </div>
    );
}

export default TeamStats;
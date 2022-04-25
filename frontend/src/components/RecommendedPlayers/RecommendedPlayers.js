import axios from "axios"
import { useEffect, useState } from "react";
import Card from "react-bootstrap/Card";

function RecommendedPlayers(props) {

    var players = props.players;

    return (
        <div>
            Recommended Players
            {
                players.map((player) =>
                    <div>
                        Name: {player.name} Height: {player.height} Position: {player.position} Position Grade: {player.positionGrade}
                    </div>
                )
            }
        </div>
    );
}

export default RecommendedPlayers;
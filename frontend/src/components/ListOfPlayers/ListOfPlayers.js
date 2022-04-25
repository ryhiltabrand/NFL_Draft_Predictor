import * as React from 'react';
import axios from "axios";
import {useEffect, useState} from "react";
import Box from '@mui/material/Box';
import { FixedSizeList } from 'react-window';
import List from '@mui/material/List';
import ListItem from '@mui/material/ListItem';
import ListItemButton from '@mui/material/ListItemButton';
import Button from '@mui/material/Button';
import ListItemText from '@mui/material/ListItemText';
import Divider from '@mui/material/Divider';
import draft from "../../data/draft.json"

function remove(player,team){
    const host = window.location.hostname;
    const port = 8000;
    const play={
        team: team.acryonm,
        playerid: player.playerid,
        pick: team.id,
    }
    axios.post(`http://${host}:${port}/draft/${play.team}/${play.playerid}/${play.pick}`).then(res =>console.log(res.data));

}

function ListOfPlayers(props) {
    const {team, draftees, setDraftees, setTeam, increment, setIncrement} = props;
    return (
        <List sx={{
            width: 1,
            bgcolor: 'background.paper',
            position: 'relative',
            overflow: 'auto',
            maxHeight: 300,
            '& ul': { padding: 0 },
          }}>
        {draftees.map((player)=>( 
                <ListItem
                    key={player.playerId}
                    secondaryAction={
                        <Button variant="text"
                            onClick={()=>{
                            remove(player,team);
                            setDraftees(draftees.filter((item)=>item.playerid!==player.playerid))
                            setIncrement(increment+1)
                            setTeam(draft[increment])
                            }}
                        >
                            DRAFT
                        </Button>
                    }>
                    <ListItemText primary={`${player.name}`}/>
                    <ListItemText primary={`${player.position}`}/>
                    <ListItemText primary={`${player.athleteGrade}`}/>
                    <ListItemText primary={`${player.positionGrade}`}/>
                    <ListItemText primary={`${player.height}`}/>
                    <ListItemText primary={`${player.weight}`}/>
                    <ListItemText primary={`${player.positionGrade}`}/>
                </ListItem>
        ))}
    </List>
    );
}

export default ListOfPlayers;
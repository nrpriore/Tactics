﻿using UnityEngine;
using System.Collections.Generic;
using System;

public class MatchData {

	public int MatchID;

	// QGU properties
	public string           Name;
	public int              Round;
	public bool             UserTurn;
	public string           MapName;
	public bool             InGameQueue;
	public bool             Finished;
	public int              UserTeam;
	public int              EnemyTeam;
	public List<MatchUnit>  AlliedUnits;
	public MatchLeader      AlliedLeader;
	public List<MatchPerk>  AlliedPerks;
	public List<MatchUnit>  EnemyUnits;
	public MatchLeader      EnemyLeader;
	public List<MatchPerk>  EnemyPerks;

	// Default constructor
	// Parses all fields necessary to describe the game to the front end
	public MatchData(Dictionary<string, object> matchData) {
		// General match information
		Name        = matchData["Name"].ToString();
    	Round       = int.Parse(matchData["Round"].ToString());
        UserTurn    = (bool)matchData["Your_Turn"];
        MapName     = matchData["Map"].ToString();
        Finished    = (bool)matchData["Finished"];
		//InGameQueue = (bool)matchData["In_Game_Queue"];
		UserTeam    = int.Parse(matchData["Your_Team"].ToString());
		EnemyTeam   = int.Parse(matchData["Enemy_Team"].ToString());

		// Get all the allied units
		AlliedUnits = new List<MatchUnit>();
		foreach(object unitData in Json.ToList(matchData["Your_Units"].ToString())){
			Dictionary<string, object> unit = Json.ToDict(unitData.ToString());

			MatchUnit alliedUnit;

			alliedUnit.ID     = int.Parse(unit["ID"].ToString());
			alliedUnit.Name   = unit["Name"].ToString();
			alliedUnit.HP     = int.Parse(unit["HP"].ToString());
			alliedUnit.PrevHP = 0;		// TODO - QGU doesn't send it
			alliedUnit.X      = int.Parse(unit["X"].ToString());
			alliedUnit.Y      = int.Parse(unit["Y"].ToString());

			AlliedUnits.Add(alliedUnit);
		}

		// Get all the allied perks
		AlliedPerks = new List<MatchPerk>();
		foreach(object perkData in Json.ToList(matchData["Your_Perks"].ToString())){
			Dictionary<string, object> perk = Json.ToDict(perkData.ToString());

			MatchPerk alliedPerk;

			alliedPerk.Tier = int.Parse(perk["Tier"].ToString());
			alliedPerk.Name = perk["Name"].ToString();

			AlliedPerks.Add(alliedPerk);
		}

		// Allied leader data
		Dictionary<string, object> leaderData = (Dictionary<string, object>)matchData["Your_Leader"];
		AlliedLeader.Name    = leaderData["Name"].ToString();
		AlliedLeader.Ability = leaderData["Ability"].ToString();

		// Get all the enemy units
		EnemyUnits = new List<MatchUnit>();
		foreach(object unitData in Json.ToList(matchData["Enemy_Units"].ToString())){
			Dictionary<string, object> unit = Json.ToDict(unitData.ToString());

			MatchUnit enemyUnit;

			enemyUnit.ID     = int.Parse(unit["ID"].ToString());
			enemyUnit.Name   = unit["Name"].ToString();
			enemyUnit.HP     = int.Parse(unit["HP"].ToString());
			enemyUnit.PrevHP = 0;		// TODO - QGU doesn't send it
			enemyUnit.X      = int.Parse(unit["X"].ToString());
			enemyUnit.Y      = int.Parse(unit["Y"].ToString());

			EnemyUnits.Add(enemyUnit);
		}

		// Enemy leader data
		leaderData = (Dictionary<string, object>)matchData["Enemy_Leader"];
		EnemyLeader.Name    = leaderData["Name"].ToString();
		EnemyLeader.Ability = leaderData["Ability"].ToString();

		// Get all the enemy perks
		EnemyPerks = new List<MatchPerk>();
		foreach(object perkData in Json.ToList(matchData["Enemy_Perks"].ToString())){
			Dictionary<string, object> perk = Json.ToDict(perkData.ToString());

			MatchPerk enemyPerk;

			enemyPerk.Tier = int.Parse(perk["Tier"].ToString());
			enemyPerk.Name = perk["Name"].ToString();

			AlliedPerks.Add(enemyPerk);
		}
	}
}

public struct MatchUnit {
	public int ID;
	public string Name;
	public int HP;
	public int PrevHP;
	public int X;
	public int Y;
}

public struct MatchLeader {
	public string Name;
	public string Ability;
}

public struct MatchPerk {
	public string Name;
	public int Tier;
}

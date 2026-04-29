init python:
    class State:
        START = "start_state"
        CHOOSE_PROJECT = "choose_project"
        HUB_EXPLORE = "hub_explore"
        VISIT_GIGA = "visit_giga"
        VISIT_RPL = "visit_rpl"
        VISIT_KCV = "visit_kcv"
        RECRUIT_GIGA = "recruit_giga"
        RECRUIT_RPL = "recruit_rpl"
        RECRUIT_KCV = "recruit_kcv"
        RECRUIT_PLASA = "recruit_plasa"
        RECRUIT_VENDING = "recruit_vending"
        RECRUIT_KORIDOR = "recruit_koridor"
        CHOOSE_LAB = "choose_lab"
        ASSEMBLE_TEAM = "assemble_team"
        HACKATHON_RESULT = "hackathon_result"
        ENDING = "ending"
        EXIT = "exit"

    def lab_rpl_label():
        if "rpl" in visited_labs:
            return "Lab RPL"
        return "Lab paling pojok"
    
    def lab_kcv_label():
        if "kcv" in visited_labs:
            return "Lab KCV"
        return "Lab disebelah Laboratorium Pemrograman"
    
    def lab_giga_label():
        if "giga" in visited_labs:
            return "Lab GIGA"
        return "Lab dekat tangga"
label start:
    label state_loop:
        if current_state == State.START:
            call start_state from _call_start_state
        elif current_state == State.CHOOSE_PROJECT:
            call choose_project_state from _call_choose_project_state

        elif current_state == State.HUB_EXPLORE:
            call hub_explore_state from _call_hub_explore_state
        elif current_state == State.VISIT_RPL:
            call visit_rpl_state from _call_visit_rpl_state
        elif current_state == State.VISIT_KCV:
            call visit_kcv_state from _call_visit_kcv_state
        elif current_state == State.VISIT_GIGA:
            call visit_giga_state from _call_visit_giga_state
        elif current_state == State.CHOOSE_LAB:
            call choose_lab_state from _call_choose_lab_state
        elif current_state == State.ASSEMBLE_TEAM:
            call assemble_team_state from _call_assemble_team_state
        elif current_state == State.RECRUIT_RPL:
            call recruit_rpl_state from _call_recruit_rpl_state
        elif current_state == State.RECRUIT_KCV:
            call recruit_kcv_state from _call_recruit_kcv_state
        elif current_state == State.RECRUIT_GIGA:
            call recruit_giga_state from _call_recruit_giga_state
        elif current_state == State.RECRUIT_PLASA:
            call recruit_plasa_state from _call_recruit_plasa_state
        elif current_state == State.RECRUIT_VENDING:
            call recruit_vending_state from _call_recruit_vending_state
        elif current_state == State.RECRUIT_KORIDOR:
            call recruit_koridor_state from _call_recruit_koridor_state
        elif current_state == State.ENDING:
            call ending_state from _call_ending_state
            

        else:
            return
        jump state_loop
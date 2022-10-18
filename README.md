Commands:

/background:
  Positional Arguments:
    set <bg_identifier>
    rotate <degrees>
    flip <veritcal, horizontal>
    transition <bg_identifier> 
      -fade_time <ms>
      -slide <direction>

/grid:
  Position Arguments:
    show
    hide
    grow
    shrink
    color (R,G,B)
    thickness <pixels>

/create
  Position Arguments:
    [pc, npc, monster, item] <name> <hp> <bg_identifier> <token_size>

/delete
  Positional Arguments:
    [pc, npc, monster, item] <name>

/move 
  Positional Arguments:
    [pc, npc, monster, item]
    Optional Arguments:
      right <units>
      up <units>
      left <units>
      down <units>
      (x, y)

/initiative
  Positional Arguments:
    <name> <init_roll> [forEach person in battle]
    next
    stop

/attack <attacker> <defender> <hit points>

/health [pc, npc, monster, item] (+,-) <x>

/ping <name>

/vision_radius
  Positional Arguments:
    set <units>
    inc <units>
    dec <units>

/quit

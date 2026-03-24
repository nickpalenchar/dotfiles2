tag: user.training_active
-
# Control commands (matched before phrase wildcard)
next: user.trainer_next()
skip: user.trainer_next()
again: user.trainer_retry()
stop training: user.trainer_stop()

# Capture anything else as the spoken phrase
<phrase>: user.trainer_record("{phrase}")

# Timeflux hands-on

## Filtering

### Filter an arbitrary signal

- Add a notch filter to remove line noise at 50 Hz.
- Add a bandpass filter to keep only frequencies between 8 and 20 Hz.
- Ensure your are able to visualize the raw and filtered signals!


```
timeflux -d graphs/filter_signal.yaml
```

:bulb: Check the [documentation](https://doc.timeflux.io/projects/timeflux-dsp/en/stable/api/timeflux_dsp/nodes/filters/index.html#timeflux_dsp.nodes.filters.IIRFilter)!

### Filter an audio signal

- Keep only the **300 Hz** component.


```
timeflux graphs/filter_audio.yaml
```

:bulb: Turn your speakers on!

## Recording

### Save to CSV

- Add a node to save the signal to a CSV file located at `data/dump.csv`.

```
timeflux graphs/record_csv.yaml
```

:bulb: Check the [documentation](https://doc.timeflux.io/en/stable/api/timeflux/nodes/debug/index.html#timeflux.nodes.debug.Dump)!

### Save to HDF5

- Add a node to save both the signal and the events to a **HDF5** file in the `data` directory.
- Make sure you allow **enough memory** to store events.

```
timeflux -d graphs/record_hdf.yaml
```

:bulb: Check the [documentation](https://doc.timeflux.io/en/stable/api/timeflux/nodes/hdf5/index.html#timeflux.nodes.hdf5.Save)
:bulb: You can generate events directly from the monitoring interface.

## Environment and templating

### Set the seed from the command line

- **Update** the following command line to set the **seed** of the random generator:

```
timeflux -d graphs/env_seed.yaml
```

:bulb: Check the [documentation](https://doc.timeflux.io/en/stable/usage/getting_started.html#environment)!

### Hyperscanning

- Instead of only one data stream, allow an **arbitrary number of devices** to connect simultaneously by using the configuration file in `config/hyperscanning.txt`.

```
timeflux -d graphs/env_hyperscanning.yaml
```

:bulb: Check the Jinja [documentation](https://jinja.palletsprojects.com/en/3.0.x/templates/#for)!
:bulb: Get inspiration from a more [complex project](https://github.com/timeflux/demos/tree/main/hyperscanning)

# Custom node

## Sine to square

- Edit `nodes/pulse.py` to **transform** an incoming sine signal into a pulse signal.
- The **width** of the pulse can be configured using the `threshold` parameter. A `0` value results in a square waveform.

```
timeflux graphs/pulse_node.yaml
```

# Machine learning

## Transformer

- Edit `estimators/pulse.py` to **transform** an incoming sine signal into a pulse signal.
- The **width** of the pulse can be configured using the `threshold` parameter. A `0` value results in a square waveform.

```
timeflux graphs/pulse_transformer.yaml
```

## Classifier

- Inspect the [P300 speller](https://github.com/timeflux/demos/tree/main/speller/P300) demo.

